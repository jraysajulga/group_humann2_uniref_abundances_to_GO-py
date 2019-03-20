import argparse
import sys
import os
import subprocess
import goatools
#from scripts.format_humann2_uniref_go_mapping import format_humann2_uniref_go_mapping


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

    tmp_data_dir = "data"
    scripts_dir = "scripts"

    print("Format HUMAnN2 UniRef50 GO mapping")
    print("==================================")
    subprocess.call(["python", scripts_dir + "/format_humann2_uniref_go_mapping.py",
                    "--uniref_go_mapping_input", args.map_file,
                    "--uniref_go_mapping_output", tmp_data_dir + "/uniref_go_mapping_output.txt",
                    "--go_names", tmp_data_dir + "/humann2_go_names.txt"])
    print("")

    print("Map to slim GO")
    print("==============")
    with open(tmp_data_dir + "/humann2_go_slim.txt", "wb") as out:
        subprocess.call(["map_to_slim.py",
         "--association_file", tmp_data_dir + "/humann2_go_names.txt",
         args.go_file,
         args.goslim_file], 
         stdout = out)
    print("")

    print("Format slim GO")
    print("==============")
    subprocess.call(["python", scripts_dir + "/format_go_correspondance.py",
        "--go_correspondance_input", tmp_data_dir + "/humann2_go_slim.txt",
        "--go_correspondance_output", tmp_data_dir + "/formatted_humann2_go_slim.txt"])
    print("")

    print("Regroup UniRef50 to GO")
    print("======================")
    subprocess.call(["humann2_regroup_table",
        "-i", args.input,
        "-f", "sum",
        "-c", tmp_data_dir + "/uniref_go_mapping_output.txt",
        "-o", tmp_data_dir + "/humann2_go_abundances.txt"])
    print("")

    print("Regroup GO to slim GO")
    print("=====================")
    subprocess.call(["humann2_regroup_table",
        "-i", tmp_data_dir + "/humann2_go_abundances.txt",
        "-f", "sum",
        "-c", tmp_data_dir + "/formatted_humann2_go_slim.txt",
        "-o", tmp_data_dir + "/humann2_slim_go_abundances.txt"])
    print("")

    print("Format slim GO abundance")
    print("========================")
    subprocess.call(["python", scripts_dir + "/format_humann2_output.py",
        "--go_slim", args.goslim_file,
        "--humann2_output", tmp_data_dir + "/humann2_slim_go_abundances.txt",
        "--molecular_function_output_file", args.goslim_mf,
        "--biological_processes_output_file", args.goslim_bp,
        "--cellular_component_output_file", args.goslim_cc])
    print("")







if __name__=="__main__":
    main()
