// Autogenerated AST node
package org.python.antlr.ast;
import org.python.antlr.PythonTree;
import org.antlr.runtime.CommonToken;
import org.antlr.runtime.Token;
import java.io.DataOutputStream;
import java.io.IOException;

public class Compare extends exprType {
    public exprType left;
    public cmpopType[] ops;
    public exprType[] comparators;

    public static final String[] _fields = new String[]
    {"left","ops","comparators"};

    public Compare(Token token, exprType left, cmpopType[] ops, exprType[]
    comparators) {
        super(token);
        this.left = left;
        this.ops = ops;
        this.comparators = comparators;
        if (comparators != null) {
            for(int
            icomparators=0;icomparators<comparators.length;icomparators++) {
                addChild(comparators[icomparators]);
            }
        }
    }

    public Compare(int ttype, Token token, exprType left, cmpopType[] ops,
    exprType[] comparators) {
        super(ttype, token);
        this.left = left;
        this.ops = ops;
        this.comparators = comparators;
        if (comparators != null) {
            for(int
            icomparators=0;icomparators<comparators.length;icomparators++) {
                addChild(comparators[icomparators]);
            }
        }
    }

    public Compare(PythonTree tree, exprType left, cmpopType[] ops, exprType[]
    comparators) {
        super(tree);
        this.left = left;
        this.ops = ops;
        this.comparators = comparators;
        if (comparators != null) {
            for(int
            icomparators=0;icomparators<comparators.length;icomparators++) {
                addChild(comparators[icomparators]);
            }
        }
    }

    public String toString() {
        return "Compare";
    }

    public String toStringTree() {
        StringBuffer sb = new StringBuffer("Compare[");
        sb.append("left=");
        sb.append(this.left);
        sb.append("ops=");
        sb.append(this.ops);
        sb.append("comparators=");
        sb.append(this.comparators);
        sb.append("]");
        return sb.toString();
    }

    public <R> R accept(VisitorIF<R> visitor) throws Exception {
        return visitor.visitCompare(this);
    }

    public void traverse(VisitorIF visitor) throws Exception {
        if (left != null)
            left.accept(visitor);
        if (comparators != null) {
            for (int i = 0; i < comparators.length; i++) {
                if (comparators[i] != null)
                    comparators[i].accept(visitor);
            }
        }
    }

    public int getLineno() {
        return getLine();
    }

    public int getCol_offset() {
        return getCharPositionInLine();
    }

}
