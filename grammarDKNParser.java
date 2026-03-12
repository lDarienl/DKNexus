// Generated from grammarDKN.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class grammarDKNParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		NUMBER=18, VARIABLE=19, WS=20;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_expr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'if'", "'('", "')'", "'{'", "'}'", "'for'", "'while'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'sin'", "'cos'", "'tan'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "NUMBER", "VARIABLE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "grammarDKN.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grammarDKNParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(6);
				statement();
				}
				}
				setState(9); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1016204L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case T__14:
			case T__15:
			case T__16:
			case NUMBER:
			case VARIABLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(11);
				expr(0);
				setState(12);
				match(T__0);
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(14);
				match(T__1);
				setState(15);
				match(T__2);
				setState(16);
				expr(0);
				setState(17);
				match(T__3);
				setState(18);
				match(T__4);
				setState(20); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(19);
					statement();
					}
					}
					setState(22); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1016204L) != 0) );
				setState(24);
				match(T__5);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(26);
				match(T__6);
				setState(27);
				match(T__2);
				setState(28);
				expr(0);
				setState(29);
				match(T__0);
				setState(30);
				expr(0);
				setState(31);
				match(T__0);
				setState(32);
				expr(0);
				setState(33);
				match(T__3);
				setState(34);
				match(T__4);
				setState(36); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(35);
					statement();
					}
					}
					setState(38); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1016204L) != 0) );
				setState(40);
				match(T__5);
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 4);
				{
				setState(42);
				match(T__7);
				setState(43);
				match(T__2);
				setState(44);
				expr(0);
				setState(45);
				match(T__3);
				setState(46);
				match(T__4);
				setState(48); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(47);
					statement();
					}
					}
					setState(50); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1016204L) != 0) );
				setState(52);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode NUMBER() { return getToken(grammarDKNParser.NUMBER, 0); }
		public TerminalNode VARIABLE() { return getToken(grammarDKNParser.VARIABLE, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarDKNListener ) ((grammarDKNListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				{
				setState(57);
				match(T__14);
				setState(58);
				match(T__2);
				setState(59);
				expr(0);
				setState(60);
				match(T__3);
				}
				break;
			case T__15:
				{
				setState(62);
				match(T__15);
				setState(63);
				match(T__2);
				setState(64);
				expr(0);
				setState(65);
				match(T__3);
				}
				break;
			case T__16:
				{
				setState(67);
				match(T__16);
				setState(68);
				match(T__2);
				setState(69);
				expr(0);
				setState(70);
				match(T__3);
				}
				break;
			case NUMBER:
				{
				setState(72);
				match(NUMBER);
				}
				break;
			case VARIABLE:
				{
				setState(73);
				match(VARIABLE);
				}
				break;
			case T__2:
				{
				setState(74);
				match(T__2);
				setState(75);
				expr(0);
				setState(76);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(100);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(98);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(80);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(81);
						match(T__8);
						setState(82);
						expr(13);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(83);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(84);
						match(T__9);
						setState(85);
						expr(12);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(86);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(87);
						match(T__10);
						setState(88);
						expr(11);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(89);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(90);
						match(T__11);
						setState(91);
						expr(10);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(92);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(93);
						match(T__12);
						setState(94);
						expr(9);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(95);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(96);
						match(T__13);
						setState(97);
						expr(8);
						}
						break;
					}
					} 
				}
				setState(102);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014h\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0004\u0000\b\b\u0000\u000b\u0000\f\u0000"+
		"\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0004\u0001\u0015\b\u0001\u000b\u0001"+
		"\f\u0001\u0016\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0004\u0001%\b\u0001\u000b\u0001\f\u0001&\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0004\u00011\b\u0001\u000b\u0001\f\u00012\u0001\u0001\u0001\u0001"+
		"\u0003\u00017\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002O\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0005\u0002c\b\u0002\n\u0002\f\u0002f\t\u0002"+
		"\u0001\u0002\u0000\u0001\u0004\u0003\u0000\u0002\u0004\u0000\u0000v\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u00026\u0001\u0000\u0000\u0000\u0004N\u0001"+
		"\u0000\u0000\u0000\u0006\b\u0003\u0002\u0001\u0000\u0007\u0006\u0001\u0000"+
		"\u0000\u0000\b\t\u0001\u0000\u0000\u0000\t\u0007\u0001\u0000\u0000\u0000"+
		"\t\n\u0001\u0000\u0000\u0000\n\u0001\u0001\u0000\u0000\u0000\u000b\f\u0003"+
		"\u0004\u0002\u0000\f\r\u0005\u0001\u0000\u0000\r7\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0005\u0002\u0000\u0000\u000f\u0010\u0005\u0003\u0000\u0000"+
		"\u0010\u0011\u0003\u0004\u0002\u0000\u0011\u0012\u0005\u0004\u0000\u0000"+
		"\u0012\u0014\u0005\u0005\u0000\u0000\u0013\u0015\u0003\u0002\u0001\u0000"+
		"\u0014\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000"+
		"\u0016\u0014\u0001\u0000\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000"+
		"\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u0019\u0005\u0006\u0000\u0000"+
		"\u00197\u0001\u0000\u0000\u0000\u001a\u001b\u0005\u0007\u0000\u0000\u001b"+
		"\u001c\u0005\u0003\u0000\u0000\u001c\u001d\u0003\u0004\u0002\u0000\u001d"+
		"\u001e\u0005\u0001\u0000\u0000\u001e\u001f\u0003\u0004\u0002\u0000\u001f"+
		" \u0005\u0001\u0000\u0000 !\u0003\u0004\u0002\u0000!\"\u0005\u0004\u0000"+
		"\u0000\"$\u0005\u0005\u0000\u0000#%\u0003\u0002\u0001\u0000$#\u0001\u0000"+
		"\u0000\u0000%&\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000&\'\u0001"+
		"\u0000\u0000\u0000\'(\u0001\u0000\u0000\u0000()\u0005\u0006\u0000\u0000"+
		")7\u0001\u0000\u0000\u0000*+\u0005\b\u0000\u0000+,\u0005\u0003\u0000\u0000"+
		",-\u0003\u0004\u0002\u0000-.\u0005\u0004\u0000\u0000.0\u0005\u0005\u0000"+
		"\u0000/1\u0003\u0002\u0001\u00000/\u0001\u0000\u0000\u000012\u0001\u0000"+
		"\u0000\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000034\u0001"+
		"\u0000\u0000\u000045\u0005\u0006\u0000\u000057\u0001\u0000\u0000\u0000"+
		"6\u000b\u0001\u0000\u0000\u00006\u000e\u0001\u0000\u0000\u00006\u001a"+
		"\u0001\u0000\u0000\u00006*\u0001\u0000\u0000\u00007\u0003\u0001\u0000"+
		"\u0000\u000089\u0006\u0002\uffff\uffff\u00009:\u0005\u000f\u0000\u0000"+
		":;\u0005\u0003\u0000\u0000;<\u0003\u0004\u0002\u0000<=\u0005\u0004\u0000"+
		"\u0000=O\u0001\u0000\u0000\u0000>?\u0005\u0010\u0000\u0000?@\u0005\u0003"+
		"\u0000\u0000@A\u0003\u0004\u0002\u0000AB\u0005\u0004\u0000\u0000BO\u0001"+
		"\u0000\u0000\u0000CD\u0005\u0011\u0000\u0000DE\u0005\u0003\u0000\u0000"+
		"EF\u0003\u0004\u0002\u0000FG\u0005\u0004\u0000\u0000GO\u0001\u0000\u0000"+
		"\u0000HO\u0005\u0012\u0000\u0000IO\u0005\u0013\u0000\u0000JK\u0005\u0003"+
		"\u0000\u0000KL\u0003\u0004\u0002\u0000LM\u0005\u0004\u0000\u0000MO\u0001"+
		"\u0000\u0000\u0000N8\u0001\u0000\u0000\u0000N>\u0001\u0000\u0000\u0000"+
		"NC\u0001\u0000\u0000\u0000NH\u0001\u0000\u0000\u0000NI\u0001\u0000\u0000"+
		"\u0000NJ\u0001\u0000\u0000\u0000Od\u0001\u0000\u0000\u0000PQ\n\f\u0000"+
		"\u0000QR\u0005\t\u0000\u0000Rc\u0003\u0004\u0002\rST\n\u000b\u0000\u0000"+
		"TU\u0005\n\u0000\u0000Uc\u0003\u0004\u0002\fVW\n\n\u0000\u0000WX\u0005"+
		"\u000b\u0000\u0000Xc\u0003\u0004\u0002\u000bYZ\n\t\u0000\u0000Z[\u0005"+
		"\f\u0000\u0000[c\u0003\u0004\u0002\n\\]\n\b\u0000\u0000]^\u0005\r\u0000"+
		"\u0000^c\u0003\u0004\u0002\t_`\n\u0007\u0000\u0000`a\u0005\u000e\u0000"+
		"\u0000ac\u0003\u0004\u0002\bbP\u0001\u0000\u0000\u0000bS\u0001\u0000\u0000"+
		"\u0000bV\u0001\u0000\u0000\u0000bY\u0001\u0000\u0000\u0000b\\\u0001\u0000"+
		"\u0000\u0000b_\u0001\u0000\u0000\u0000cf\u0001\u0000\u0000\u0000db\u0001"+
		"\u0000\u0000\u0000de\u0001\u0000\u0000\u0000e\u0005\u0001\u0000\u0000"+
		"\u0000fd\u0001\u0000\u0000\u0000\b\t\u0016&26Nbd";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}