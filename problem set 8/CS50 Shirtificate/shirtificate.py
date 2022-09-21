from fpdf import FPDF


class PDF(FPDF):
    def shirt(self, name):
        # print title
        self.set_font("Courier", "B", 50)
        self.cell(0, 70, "CS50 Shirtificate", align = "C")
        self.ln(20)
        # print image
        self.image("shirtificate.png", x = 5, y = 70, w =200)
        # print name
        self.set_font("Times", "B", 30)
        self.set_text_color(255,255,255)
        self.cell(0, 220, f"{name} took CS50", align = "C")



# Instantiation of inherited class
name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.shirt(name)
pdf.output("shirtificate.pdf")


