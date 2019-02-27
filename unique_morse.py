class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
        morse_list = []
        for word in words:
            new_word = ""
            for letter in word:
                new_word += morse_dict[letter]
            morse_list.append(new_word)
        morse_set = set(morse_list)
        return len(morse_set)
