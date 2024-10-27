#let config = toml("config.toml")

#let name = config.name
#let links = (
  email: link("mailto:" + config.email),
  phone: link("tel:" + config.phone),
)
#let date = datetime(year: 2022, month: 9, day: 14)

// page layout

#set page(margin: 1.2in, paper: "a4")
#set text(font: config.font, size: config.size * 1pt, lang: "eng")
#set par(justify: true, first-line-indent: 2em)
#set list(marker: "", body-indent: 0em)
#show link: underline


#let letter_date = [20#super[th] September 2024]

// your details
#h(1fr) #box[
  #set align(left)
  - #name
  - #links.email
  - #links.phone
  - #letter_date
]

#v(1em)

// their details
- Santa Claus and Co
- 123 Elf Road
- North Pole

#v(1em)

// content

#par(first-line-indent: 0em)[Dear Hiring Manager,]

I am writing to express my interest in the Senior Security Engineer position at your organization. With over a decade of experience in system architecture and security engineering, I have developed a comprehensive skill set that aligns perfectly with your requirements.

At Pied Piper, I served as VP of Architecture & Security, where I designed and implemented a revolutionary decentralized internet infrastructure. This role required extensive knowledge of distributed systems, security protocols, and scalable architecture. I successfully protected our network against numerous sophisticated cyber attacks while maintaining optimal system performance.


#par(first-line-indent: 0em)[
  Yours faithfully,
]

#name
