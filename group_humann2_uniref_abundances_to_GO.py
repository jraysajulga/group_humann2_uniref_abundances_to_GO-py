import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    help = 'Path to file with UniRef50 gene family abundance (HUMAnN2 output)')
parser.add_argument('-m',
                    help = 'Path to file which will contain GO slim term'
                            'abundances corresponding to molecular functions')
parser.add_argument('-b',
                    help = 'Path to file which will contain GO slim term'
                            'abundances corresponding to biological processes')
parser.add_argument('-c',
                    help = 'Path to file which will contain GO slim term'
                            'abundances corresponding to cellular components')



parser.add_argument('-a',
                    help = 'Path to basic Gene Ontology file')
parser.add_argument('-s',
                    help = 'Path to basic slim Gene Ontology file')
parser.add_argument('-u',
                    help = 'Path to file with HUMAnN2 correspondence'
                            ' between UniRef50 and GO')
parser.add_argument('-g',
                    help = 'Path to GoaTools scripts')
parser.add_argument('-p',
                    help = 'Path to HUMAnN2 scripts')
parser.add_argument('-h',
                    help = 'Print this help message')



args = parser.parse_args()

print(args.echo)

