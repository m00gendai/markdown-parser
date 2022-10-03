Custom markdown to HTML5 parser.

Vercel blog templates with markdown files for nextjs blogs do not suffice, as I require to insert HTML and React Components into the blog posts.
And .mdx files are a pain to get working.

So I created my own parser to transform my custom markdown to valid HTML5.
It is use case specific so use at your own risk. Will be enhanced on an as-needed basis.

- Strings prefixed with `###` get wrapped in `<h1>...</h1>`.
- React components are syntaxed as `<component_name component_prop ... >` in the markdown file and are converted to `<component_name prop={...} prop={...} />` depending on the component (hence use case specific).
- Raw HTML is detected based on opening and closing HTML5 tags and is inserted as is: 
  - `<div className={s.style}></div>` is inserted as `<div className={s.style}></div>` and `<img src="hello.jpg" />` is inserted as `<img src="hello.jpg" />`.

Everything else gets wrapped in `<p></p>`, including newline characters.

HTML5 and string on the same line, e.g. `<img src="hello.jpg" /> this is an image`, will be converted to `<p><img src="hello.jpg" /> this is an image</p>.
To avoid this, place HTML5 on a separate line if it being wrapped in `<p></p>`is not desired.

HTML5 tags courtesy of [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
