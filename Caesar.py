class Caesar:
	"""docstring for Encrypt"""
	def __init__(self,plainText,key):
		self.plainText = str.lower(plainText)
		self.key = key
	def encrypt(self):
		abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
		chiperText = ""
		for words in self.plainText:
			wordsIndex = abjad.find(words)+self.key
			chiperText= chiperText+abjad[wordsIndex]

		return chiperText

	def decrypt(self):
		abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
		chiperText = ""
		for words in self.plainText:
			wordsIndex = abjad.find(words)-self.key
			chiperText= chiperText+abjad[wordsIndex]
		return chiperText

		