import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import htmlinterp
import graphics as graphics
import jstokens



webpage = """<html>
<h1>JavaScript That Produces HTML</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">
write("<b>This whole sentence should be bold, and the concepts in this problem touch on the <a href='http://en.wikipedia.org/wiki/Document_Object_Model'>Document Object Model</a>, which allows web browsers and scripts to <i>manipulate</i> webpages.</b>");
</script>
... and this paragraph finishes in HTML.
</p>
<hr> </hr> <!-- draw a horizontal bar -->
<p>
Now we will use JavaScript to display even numbers in <i>italics</i> and
odd numbers in <b>bold</b>. <br> </br>
<script type="text/javascript">
function tricky(i) {
  if (i <= 0) {
    return i;
  } ;
  if ((i % 2) == 1) {
    write("<b>");
    write(i);
    write("</b>");
  } else {
    write("<i>");
    write(i);
    write("</i>");
  }
  return tricky(i - 1);
}
tricky(10);
</script>
</p>
</html>"""


htmllexer = lex.lex(module=htmltokens)
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml")
ast = htmlparser.parse(webpage,lexer=htmllexer)
jslexer = lex.lex(module=jstokens)
graphics.initialize() # Enables display of output.
htmlinterp.interpret(ast)
graphics.finalize()