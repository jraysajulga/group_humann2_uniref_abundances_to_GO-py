import argparse

def main():

    parser = argparse.ArgumentParser(description = "Runs scripts to group UniRef50 "
        "abundances obtained using main HUMANn2 (Gene families) to GO slim terms.")
    parser._action_groups.pop()

    parser_required = parser.add_argument_group("Required options")
    parser_required.add_argument("-i", type = str, dest = "input",
                                   help = "Path to file with UniRef50 gene family "
                                           "abundance (HUMAnN2 output)",
                                    required = True)
    parser_required.add_argument("-m", type = str, dest = "goslim_mf",
                                    help = "Path to file which will contain GO slim term "
                                            "abundances corresponding to molecular functions",
                                    required = True)
    parser_required.add_argument("-b", type = str, dest = "goslim_bp",
                                    help = "Path to file which will contain GO slim term "
                                            "abundances corresponding to biological processes",
                                    required = True)
    parser_required.add_argument("-c", type = str, dest = "goslim_cc",
                                    help = "Path to file which will contain GO slim term "
                                            "abundances corresponding to cellular components",
                                    required = True)
    
    parser_optional = parser.add_argument_group("Optional arguments")
    parser_optional.add_argument("-a", type = str, dest = "go_file",
                                    help = "Path to basic Gene Ontology file")
    parser_optional.add_argument("-s", type = str, dest = "goslim_file",
                                    help = "Path to basic slim Gene Ontology file")
    parser_optional.add_argument("-u", type = str, dest = "map_file",
                                    help = "Path to file with HUMAnN2 correspondence"
                                            " between UniRef50 and GO")
    parser_optional.add_argument("-g", type = str,
                                    help = "Path to GOAtools scripts")
    parser_optional.add_argument("-p", type = str,
                                    help = "Path to HUMAnN2 scripts")

    args = parser.parse_args()

    print(args.input)


if __name__=="__main__":
    main()
