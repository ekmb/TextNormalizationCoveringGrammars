import pynini
from pynini.lib import rewrite

example = {'tn': "28", 'itn': "двадцать восемь"}

grammar_dir = '/home/ebakhturina/itn_cg/TextNormalizationCoveringGrammars/src'
grammars = {'verbalizer/verbalizer.far': ['VERBALIZER']}

eng_final_fst = pynini.Far(f'{grammar_dir}/en/verbalizer/verbalizer.far', mode='r')['VERBALIZER']
ru_final_fst = pynini.Far(f'{grammar_dir}/ru/verbalizer/verbalizer.far', mode='r')['VERBALIZER']
ru_numbers_fst = pynini.Far(f'{grammar_dir}/ru/verbalizer/numbers.far', mode='r')['CARDINAL_DEFAULT']

print('NORMALIZATION:')
print('Input:', example['tn'])
print('ENG:', rewrite.rewrites(example['tn'], eng_final_fst))
print('RU:', rewrite.rewrites(example['tn'], ru_final_fst))
print('-' * 60)
print('INVERSE NORMALIZATION:')
invert = ru_numbers_fst.invert()
print('all:', rewrite.rewrites(example['itn'], invert.optimize()))
print('top:', rewrite.top_rewrite(example['itn'], invert.optimize()))