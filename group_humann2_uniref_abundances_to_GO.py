import argparse

def main():

    parser = argparse.ArgumentParser(description = "Runs scripts to group UniRef50 "
        "abundances obtained using main HUMANn2 (Gene families) to GO slim terms.")

    # Required arguments
    parser.add_argument("-i", "--input", type = str,
                        help = "Path to file with UniRef50 gene family "
                               "abundance (HUMAnN2 output)",
                        required = True)
    parser.add_argument("-m", type = str,
                        help = "Path to file which will contain GO slim term "
                                "abundances corresponding to molecular functions",
                        required = True)
    parser.add_argument("-b", type = str,
                        help = "Path to file which will contain GO slim term "
                                "abundances corresponding to biological processes",
                        required = True)
    parser.add_argument("-c", type = str,
                        help = "Path to file which will contain GO slim term "
                                "abundances corresponding to cellular components",
                        required = True)
    # Optional arguments
    parser.add_argument("-a", type = str,
                        help = "Path to basic Gene Ontology file")
    parser.add_argument("-s", type = str,
                        help = "Path to basic slim Gene Ontology file")
    parser.add_argument("-u", type = str,
                        help = "Path to file with HUMAnN2 correspondence"
                                " between UniRef50 and GO")
    parser.add_argument("-g", type = str,
                        help = "Path to GoaTools scripts")
    parser.add_argument("-p", type = str,
                        help = "Path to HUMAnN2 scripts")


    args = parser.parse_args()


if __name__=="__main__":
    main()
