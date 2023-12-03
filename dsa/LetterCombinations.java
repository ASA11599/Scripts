import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class LetterCombinations {

    private static final Map<String, List<String>> DIGIT_LETTERS = new HashMap<String, List<String>>();;

    static {
        LetterCombinations.DIGIT_LETTERS.put("2", List.of("a", "b", "c"));
        LetterCombinations.DIGIT_LETTERS.put("3", List.of("d", "e", "f"));
        LetterCombinations.DIGIT_LETTERS.put("4", List.of("g", "h", "i"));
        LetterCombinations.DIGIT_LETTERS.put("5", List.of("j", "k", "l"));
        LetterCombinations.DIGIT_LETTERS.put("6", List.of("m", "n", "o"));
        LetterCombinations.DIGIT_LETTERS.put("7", List.of("p", "q", "r", "s"));
        LetterCombinations.DIGIT_LETTERS.put("8", List.of("t", "u", "v"));
        LetterCombinations.DIGIT_LETTERS.put("9", List.of("w", "x", "y", "z"));
    }

    public static List<String> find(String digits) {
        List<String> combinations = new LinkedList<String>();
        combinations.add("");
        for (int i = 0; i < digits.length(); i++) {
            String d = digits.substring(i, i + 1);
            List<String> newCombinations = new LinkedList<String>();
            while (!combinations.isEmpty()) {
                String c = combinations.remove(0);
                List<String> dLetters = LetterCombinations.DIGIT_LETTERS.get(d);
                for (String l : dLetters) {
                    newCombinations.add(c + l);
                }
            }
            combinations.addAll(newCombinations);
        }
        if (combinations.size() == 1) combinations.remove(0);
        return combinations;
    }

    public static void main(String[] args) {
        System.out.println(LetterCombinations.find("445"));
    }

}
