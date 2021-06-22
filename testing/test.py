import pynini
from pynini.lib import rewrite

grammar_dir = '/home/ebakhturina/itn_cg/TextNormalizationCoveringGrammars/src'

eng_final_fst = pynini.Far(f'{grammar_dir}/en/verbalizer/verbalizer.far', mode='r')['VERBALIZER']
ru_final_fst = pynini.Far(f'{grammar_dir}/ru/verbalizer/verbalizer.far', mode='r')['VERBALIZER']
ru_numbers_fst = pynini.Far(f'{grammar_dir}/ru/verbalizer/numbers.far', mode='r')['CARDINAL_DEFAULT']

example = {'tn': "23", 'itn': "двадцать восемь"}
print('NORMALIZATION:')
print('Input:', example['tn'])
print('ENG:', rewrite.rewrites(example['tn'], eng_final_fst))
print('RU:', rewrite.rewrites(example['tn'], ru_final_fst))
print('-' * 60)
print('INVERSE NORMALIZATION:')
invert = ru_numbers_fst.invert().optimize()
print('RU:', rewrite.top_rewrite(example['itn'], invert))

try:
    other_numbers_fst = pynini.Far(f'{grammar_dir}/other/verbalizer/numbers.far', mode='r')['CARDINAL_DEFAULT']
    print('Other:', rewrite.top_rewrite(example['itn'], other_numbers_fst.invert().optimize()))
except:
    print('grammar for other language is not found')

for v in rewrite.rewrites("1000", ru_final_fst):
    if "тысяч" in v:
        print(v)
