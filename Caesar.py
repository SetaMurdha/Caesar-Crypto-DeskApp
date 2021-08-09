class Caesar:
	
	def __init__(self,plainText,key):
		self.plainText = str.lower(plainText)
		self.key = key
	def encrypt(self):
		abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
		chiperText = ""
		for words in self.plainText:
			wordsIndex = (abjad.find(words)+self.key)%len(abjad)
			chiperText= chiperText+abjad[wordsIndex]
		return chiperText

	def decrypt(self):
		abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
		chiperText = ""
		for words in self.plainText:
			wordsIndex = (abjad.find(words)-self.key)%len(abjad)
			chiperText= chiperText+abjad[wordsIndex]
		return chiperText
