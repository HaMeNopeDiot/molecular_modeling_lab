#import "@preview/codelst:2.0.2": sourcecode

#let line_margin = 1.15em

#let template(doc) = {
  let in-ref = state("in-ref", false)
  show ref: it => in-ref.update(true) + it + in-ref.update(false)
  let sup(fig, ref) = (supplement: context if in-ref.get() { ref } else { fig })
  show figure.where(kind: image): set figure(..sup("Рис.", "рис."))
  show figure.where(kind: image): set figure.caption(separator: [ --- ])
  show figure.where(kind: table): set figure(..sup("Таблица", "табл."))
  show figure.where(kind: table): set figure.caption(position: top, separator: [ --- ])
  show figure.caption.where(kind: table): set align(left)
  show figure.where(kind: raw): set figure(..sup("Листинг", "лист."))
  show raw: set text(
    font: "New Computer Modern",
    size: 12pt,
  )
  show figure: set block(breakable: true)
  show heading: set block(below: line_margin)

  doc
}

#show: template

#set text(
    font: "New Computer Modern",
    size: 12pt,
)

#set math.equation(numbering: "(1)")

#set par(
    justify: true,
    first-line-indent: (
        amount: 1.25cm,
        all: true,
    ),
    spacing: line_margin,
    leading: line_margin,
)

#include "title.typ"

#set heading(numbering: "1.")

#set page(
  header: stack(
      spacing: 4%,
      stack(
          dir: ltr,
          align(left, [_Voronezh State University, AMM_]),
          align(right, [_Dudkin I.A., Sviridova S.Yu., Starukhin D.M._]),
      ),
    line(length: 100%),
    line(length: 100%),
  ),
  footer: context [
    #stack(
      spacing: 4%,
      line(length: 100%),
      [],
      align(center, counter(page).display(
          "1",
        )
      )
    )
  ],
  footer-descent: 2mm,
  header-ascent: 2mm,
  margin: (
    top: 2.2cm,
    bottom: 2.2cm,
    right: 1cm,
    left: 3cm,
  )
)

#outline(
  title: [Оглавление]
)

#pagebreak()

#include "report.typ"

#pagebreak()

#set heading(numbering: none)
= Приложение 1. Листинг программы создания статического кадра

#sourcecode(lang: "python")[
    #raw(read("tt.py"))
]

#pagebreak()

= Приложение 2. Листинг программы создания анимации процесса релаксации многоатомной системы

*dislin_picture.py*

#sourcecode(lang: "python")[
    #raw(read("dislin_picture.py"))
]

*png2mp4.py*

#sourcecode(lang: "python")[
    #raw(read("png2mp4.py"))
]
