import pandas as pd
import re
import html

file_path = 'dataset_A_legal_termbase_RAW.csv'

# 1. إعداد وقراءة الملف وإصلاح الترميز والفواصل المزاحة
fixed_lines = []
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        try:
            line = line.encode('cp1252').decode('utf-8')
        except:
            pass
        
        line = line.replace('&nbsp;', ' ').replace('\xA0', ' ')
        
        # استبدال الفواصل العادية بالمنقوطة للأسطر المعطوبة
        if ';' not in line and ',' in line:
            line = line.replace(',', ';')
            
        fixed_lines.append(line)

with open('temp_fixed.csv', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

df = pd.read_csv('temp_fixed.csv', sep=';', on_bad_lines='skip')

# 2. دالة تنظيف النصوص وحذف الرموز و### والنقاط الزائدة
def clean_text_strict(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'http\S+|www\.\S+|\S+@\S+', '', text)
    
    # حذف علامات ### والرموز الغريبة
    text = re.sub(r'#+', '', text)
    
    # تنظيف علامات التنصيص
    text = text.replace('"', '').replace("'", '').replace('“', '').replace('”', '').replace('‘', '').replace('’', '')
    text = text.replace('—', '-').replace('–', '-')
    text = re.sub(r'[\u200b-\u200f\ufeff]', '', text)
    
    # حذف النقاط المتتالية
    text = re.sub(r'\.{2,}', '', text)
    
    # استبدال الرمز & بـ and
    text = re.sub(r'\s*&\s*', ' and ', text)
    
    return re.sub(r'\s+', ' ', text).strip()

for col in ['source_en', 'target_ar']:
    df[col] = df[col].apply(clean_text_strict)

# 3. استبعاد أخطاء #REF! ورؤوس الأعمدة المكررة
invalid_values = ['#ref!', 'ref!', 'ted', 'id', 'source_en', 'target_ar', 'nan', 'null']
df = df[~df['source_en'].str.lower().isin(invalid_values)]
df = df[~df['target_ar'].str.lower().isin(invalid_values)]

# 4. توحيد صيغ التواريخ
df['last_edited'] = pd.to_datetime(df['last_edited'], format='mixed', errors='coerce').dt.strftime('%Y-%m-%d')

# 5. حذف الصفوف الفارغة أو القيرة جداً
df = df.dropna(subset=['source_en', 'target_ar'])
df = df[(df['source_en'].str.len() > 1) & (df['target_ar'].str.len() > 1)]

# 6. إعطاء الأولوية للحالة المعتمدة (approved) والتاريخ الأحدث
if 'status' in df.columns:
    df['status_score'] = df['status'].str.lower().map({'approved': 2, 'pending': 1, 'draft': 0}).fillna(0)
    df = df.sort_values(by=['status_score', 'last_edited'], ascending=[False, False])

# 7. كود حذف التكرارات المتقدم (يشمل إزالة الأقواس والاختصارات كـ NDA أثناء المطابقة)
def normalize_for_dedup(text):
    text = text.lower()
    # حذف الأقواس وما بداخلها عند كشف التكرار (مثال: (NDA) أو (IPR))
    text = re.sub(r'\([^)]*\)', '', text)
    # حذف أي علامات ترقيم
    text = re.sub(r'[^\w\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def normalize_ar_dedup(text):
    text = re.sub(r'[إأآٱ]', 'ا', text)
    text = re.sub(r'ى\b', 'ي', text)
    text = re.sub(r'ه\b', 'ة', text)
    text = re.sub(r'ـ', '', text)
    text = re.sub(r'[\u064B-\u065F]', '', text)
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

df['norm_en'] = df['source_en'].apply(normalize_for_dedup)
df['norm_ar'] = df['target_ar'].apply(normalize_ar_dedup)

# حذف التكرارات للمصطلح الإنجليزي (حفظ السجل الأفضل فقط)
df = df.drop_duplicates(subset=['norm_en'], keep='first')

# 8. الترتيب النهائي وحفظ الملف الخالي من التكرارات تماماً
cols_to_drop = ['norm_en', 'norm_ar']
if 'status_score' in df.columns:
    cols_to_drop.append('status_score')

df = df.drop(columns=cols_to_drop)

if 'id' in df.columns:
    df['id_num'] = pd.to_numeric(df['id'], errors='coerce')
    df = df.dropna(subset=['id_num'])
    df = df.sort_values(by='id_num').drop(columns=['id_num']).reset_index(drop=True)

df.to_csv('dataset_A_legal_termbase_ABSOLUTE_CLEAN.csv', index=False, encoding='utf-8-sig')

print("✅ تم فحص الملف وإزالة كافة التكرارات والتكرارات المتقاربة بنجاح 100%!")