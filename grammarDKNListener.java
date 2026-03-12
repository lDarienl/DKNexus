// Generated from grammarDKN.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link grammarDKNParser}.
 */
public interface grammarDKNListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link grammarDKNParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(grammarDKNParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarDKNParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(grammarDKNParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarDKNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(grammarDKNParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarDKNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(grammarDKNParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarDKNParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(grammarDKNParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarDKNParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(grammarDKNParser.ExprContext ctx);
}