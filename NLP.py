class Sentence :

    def __init__(self, sentence):
      self.sentence = sentence
      self.idx = 0

    def __str__(self):
      return self.sentence.split()

    def __repr__(self):
      return '"{}".split()'.format(self.sentence)

    def __iter__(self) : 
      return self

    def __next__(self) :
        self.idx += 1
        if self.idx < len(Sentence(self.sentence).__str__()) :
            self.bigram = Sentence(self.sentence).__str__()[self.idx-1:self.idx+1]
            return self.bigram
        raise StopIteration

class Word :
    def __init__(self, word):
      self.word = word

    def __str__(self, sentence, position) :
      l = Sentence(sentence).__str__()
      l.insert(position, self.word) # insert word into list
      return ' '.join(l)  # return back sentence

    def __repr__(self, sentence, position) :
      return '"{}".insert({},{})'.format(sentence, position, self.word)

print(Sentence("This is a test").__str__())
print(Sentence("This is a test").__repr__())

print(Word("dog").__str__('I like', 2))
print(Word("dog").__repr__('I like', 2))

for bigram in Sentence('My name is Brian'):
  print(bigram)