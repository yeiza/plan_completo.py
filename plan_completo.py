from fpdf import FPDF
import pandas as pd

# Crear clase personalizada para diseño
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(255, 0, 0)  # Rojo
        self.cell(0, 10, 'ALIMENTACIÓN TEMPORADA AaB. YEIZA FÁTIMA RODRIGUES RODRIGUES', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(255, 0, 0)  # Rojo
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_image(self, image_path):
        try:
            self.image(image_path, w=100)
            self.ln(10)
        except:
            self.ln(10)

    def add_text(self, text):
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, text)
        self.ln(5)

# Iniciar PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Añadir tabla del plan semanal desde un DataFrame (ejemplo simple)
pdf.chapter_title('Plan Semanal')
df = pd.read_excel('PlanSemanal.xlsx')  # Asegúrate de tener el archivo .xlsx con los datos
for i in range(len(df)):
    pdf.add_text(f"{df.loc[i, 'Día']}: {df.loc[i, 'Comida']} / {df.loc[i, 'Cena']}")

# Añadir macros aproximados
pdf.chapter_title('Macros por Comida (aprox)')
pdf.add_text("""
Desayunos: 350-400 kcal / 15g proteína
Comidas principales: 550-600 kcal / 35g proteína
Cenas: 500-550 kcal / 30g proteína
""")

# Recetario con diseño
recetas = [
    {
        "titulo": "Pasta integral con boloñesa",
        "texto": "1. Cocina la pasta.\n2. Sofríe la cebolla y ajo.\n3. Añade carne, luego tomate y especias.\n4. Mezcla y sirve.",
        "imagen": "imagenes/pasta.jpg"
    },
    {
        "titulo": "Bulgur con pollo y verduras",
        "texto": "1. Cocina bulgur.\n2. Saltea pollo y verduras.\n3. Mezcla todo y sirve caliente.",
        "imagen": "imagenes/bulgur.jpg"
    },
    # Puedes seguir añadiendo las demás recetas...
]

pdf.chapter_title('Recetario')
for receta in recetas:
    pdf.chapter_title(receta["titulo"])
    pdf.add_image(receta["imagen"])
    pdf.add_text(receta["texto"])

# Guardar el PDF
pdf.output('Plan_Recetario_Completo.pdf')
print("PDF generado exitosamente.")