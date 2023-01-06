#https://github.com/bvalgard/create-pdf-with-python-fpdf2
#code from youtube video

from fpdf import FPDF

title = 'Lecture Notes'


class PDF(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'B', 15)
        # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_draw_color(0, 80, 180) # border = blue
        self.set_fill_color(230, 230, 0) # background = yellow
        self.set_text_color(220, 50, 50) # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Set font color grey
        self.set_text_color(169,169,169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    # Adding chapter title to start of each chapter
    def chapter_title(self, ch_num, ch_title):
        # set font
        self.set_font('helvetica', '', 12)

        # background color
        self.set_fill_color(200, 220, 255)

        # Chapter title
        chapter_title = f'Interval {ch_num}min : {ch_title}'


        self.cell(0, 5, chapter_title, ln=1, fill=1)
        # line break
        self.ln()

    # Chapter content
    def chapter_body(self, body):
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, body)
        # line break
        self.ln()
        # end each chapter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, 'Interval Over')
        self.ln()

    def print_chapter(self, ch_num, ch_title, name):
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)






