from lib.text_encoders import CharacterEncoder
from lib.text_encoders import UNKNOWN_TOKEN
from lib.text_encoders.reserved_tokens import RESERVED_ITOS


def test_character_encoder():
    sample = ['The quick brown fox jumps over the lazy dog']
    encoder = CharacterEncoder(sample)
    input_ = 'English-language pangram'
    output = encoder.encode(input_)
    assert encoder.vocab_size == len(set(list(sample[0].lower()))) + len(RESERVED_ITOS)
    assert len(output) == len(input_)
    assert encoder.decode(output) == input_.replace('-', UNKNOWN_TOKEN).lower()


def test_character_encoder_min_occurrences():
    sample = ['The quick brown fox jumps over the lazy dog']
    encoder = CharacterEncoder(sample, min_occurrences=10)
    input_ = 'English-language pangram'
    output = encoder.encode(input_)
    assert encoder.decode(output) == ''.join([UNKNOWN_TOKEN] * len(input_))
