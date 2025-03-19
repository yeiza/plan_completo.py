from fpdf import FPDF

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
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

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

# *1. Plan Semanal con Desayunos*
pdf.chapter_title('Plan Semanal')

# Plan Semanal con Desayunos
plan_semanal = [
    ("Lunes", "Desayuno: Yogur con muesli (150g yogur, 40g muesli) o fruta congelada (150g)\nComida: Pasta integral con boloñesa (150g pasta, 120g carne picada)", "Cena: Pasta integral con boloñesa (150g pasta, 120g carne picada)"),
    ("Martes", "Desayuno: Tostadas de pan integral con aguacate (1/2 aguacate), queso cottage (50g) y tomate (1)\nComida: Bulgur con pollo y verduras (130g bulgur, 120g pollo, 100g verduras)", "Cena: Bulgur con pollo y verduras (130g bulgur, 120g pollo, 100g verduras)"),
    ("Miércoles", "Desayuno: Yogur con muesli (150g yogur, 40g muesli) o fruta congelada (150g)\nComida: Ensalada de garbanzos con atún (100g garbanzos, 100g atún)", "Cena: Carne picada con verduras (130g carne picada, 150g verduras)"),
    ("Jueves", "Desayuno: Tostadas de pan integral con aguacate (1/2 aguacate), queso cottage (50g) y tomate (1)\nComida: Pasta integral con boloñesa (150g pasta, 120g carne picada)", "Cena: Pasta integral con boloñesa (150g pasta, 120g carne picada)"),
    ("Viernes", "Desayuno: Yogur con muesli (150g yogur, 40g muesli) o fruta congelada (150g)\nComida: Bulgur con pollo y verduras (130g bulgur, 120g pollo, 100g verduras)", "Cena: Bulgur con pollo y verduras (130g bulgur, 120g pollo, 100g verduras)"),
    ("Sábado", "Desayuno: Tostadas de pan integral con aguacate (1/2 aguacate), queso cottage (50g) y tomate (1)\nComida: Ensalada de garbanzos con atún (100g garbanzos, 100g atún)", "Cena: Carne picada con verduras (130g carne picada, 150g verduras)"),
    ("Domingo", "Desayuno: Yogur con muesli (150g yogur, 40g muesli) o fruta congelada (150g)\nComida: Pasta integral con boloñesa (150g pasta, 120g carne picada)", "Cena: Pasta integral con boloñesa (150g pasta, 120g carne picada)"),
]

for dia, desayuno, cena in plan_semanal:
    pdf.add_text(f"{dia}:\n{desayuno} / {cena}")
    pdf.ln(5)

# *2. Recetario con Macros y Gramos*
pdf.chapter_title('Recetario')
recetas = [
    {
        "titulo": "Pasta integral con boloñesa",
        "texto": "1. Cocina la pasta (150g).\n2. Sofríe la cebolla y ajo.\n3. Añade carne (120g), luego tomate y especias.\n4. Mezcla todo y sirve.\n\nMacros por ración:\nCalorías: 550 kcal\nCarbohidratos: 70g\nProteínas: 35g\nGrasas: 15g",
        "imagen": "imagenes/pasta.jpg"
    },
    {
        "titulo": "Bulgur con pollo y verduras",
        "texto": "1. Cocina bulgur (130g).\n2. Saltea pollo (120g) y verduras (100g).\n3. Mezcla todo y sirve caliente.\n\nMacros por ración:\nCalorías: 500 kcal\nCarbohidratos: 55g\nProteínas: 40g\nGrasas: 12g",
        "imagen": "imagenes/bulgur.jpg"
    },
    {
        "titulo": "Ensalada de garbanzos con atún",
        "texto": "1. Escurre los garbanzos (100g) y atún (100g).\n2. Mezcla con cebolla, tomate y pepino.\n3. Aliña con aceite y vinagre.\n\nMacros por ración:\nCalorías: 350 kcal\nCarbohidratos: 35g\nProteínas: 30g\nGrasas: 10g",
        "imagen": "imagenes/ensalada.jpg"
    },
    {
        "titulo": "Carne picada con verduras",
        "texto": "1. Cocina la carne picada (130g).\n2. Agrega zanahorias, guisantes y pimientos (150g).\n3. Cocina hasta que esté bien hecho.\n\nMacros por ración:\nCalorías: 450 kcal\nCarbohidratos: 35g\nProteínas: 35g\nGrasas: 20g",
        "imagen": "imagenes/carne.jpg"
    },
]

for receta in recetas:
    pdf.chapter_title(receta["titulo"])
    pdf.add_image(receta["imagen"])
    pdf.add_text(receta["texto"])

# *3. Lista de la compra con precios*
pdf.chapter_title('Lista de la Compra')
pdf.add_text("""
- Pasta integral: 500g
- Carne picada (vacuno): 500g
- Atún en conserva: 2 latas
- Garbanzos: 400g
- Bulgur: 250g
- Verduras: zanahorias, guisantes, pimientos, cebolla, tomate
- Aceite de oliva: 250ml
- Especias y condimentos
- Yogur natural: 1L
- Pan integral: 1 paquete
- Frutos secos: 100g
""")

# Guardar PDF
pdf.output("plan_semanal.pdf")