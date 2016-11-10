import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import jsinterp
import graphics as graphics
import jstokens
import jsgrammar

htmllexer = lex.lex(module=htmltokens)
htmlparser = yacc.yacc(module=htmlgrammar, tabmodule = "parsetabhtml")
jslexer = lex.lex(module=jstokens)
jsparser = yacc.yacc(module = jsgrammar, tabmodule = "parsetabjs")

def interpret(webpage):
    for node in webpage:
        nodetype = node[0]
        if nodetype == "word-element":
            graphics.word(node[1])
        elif nodetype == "tag-element":
            tagname = node[1]
            tagargs = node[2]
            subpage = node[3]
            closetagname = node[4]
            if (tagname != closetagname):
                graphics.warning("(mistmatched" + tagname + "" + closetagname + ")")
            else:
                graphics.begintag(tagname, tagargs)
                interpret(subpage)
                graphics.endtag()
        elif nodetype == "javascript-element":
            jstext = node[1]
            jspage = jsparser.parse(jstext, lexer=jslexer)
            result = jsinterp.interpret(jspage)
            htmlast = htmlparser.parse(result, lexer=htmllexer)
            interpret(htmlast)

# htmlast = htmlparser.parse(webpage, lexer=htmllexer)
# graphics.initialize()
# interpret(htmlast)
# graphics.finalize()