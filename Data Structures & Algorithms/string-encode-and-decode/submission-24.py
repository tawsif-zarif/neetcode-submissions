class Solution:

    def encode(self, strs: List[str]) -> str:
        changed_strings = []
        for item in strs:
            length = len(item)
            item = f'{length}#' + item
            changed_strings.append(item)
            
        separator = ""
        encoded_string = separator.join(changed_strings)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decode_dict = {}
        decoded_string = []
        i = 0
        temp_number = []
        while i < len(s):
            if s[i].isdigit():
                temp_number.append(s[i])
                i += 1
            elif s[i] == '#':
                separator = ""
                charcount = int(separator.join(temp_number))
                extract_string = []
                extract_string.extend(s[i+1:(i+charcount+1)])
                string_decoded = separator.join(extract_string)
                decoded_string.append(string_decoded)
                temp_number = []
                i += (charcount + 1)
        return decoded_string