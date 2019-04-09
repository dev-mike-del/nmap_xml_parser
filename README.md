# Nmap xml parser

This Python3 script parses an xml file created by the Nmap command "nmap -A -T4 -oX path_to/xml_file_name.xml your_research_target.com"

## Getting Started

Substitute "path_to/xml_file_name.xml" and "your_research_target.com" with the correct information.

You can use this script to turn an nmap xml file (specified above) into a python dictionary or you can use it to create a python dictionary of the differences between two different Nmap xml file. 

Once you have an xml file you can run this file in the interactive mode (python3 -i this_script_name.py). Then, use your xml path with the 'get_root(path)'function and the result of that with the 'get_dict(root)' function.

## Built With

* [Python 3](https://www.python.org/) - Language used
* [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) - The ElementTree XML API used to parse xml files
* [README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - Creatd by Billie Thompson and published on GitHubGist

## Authors

* **dev-mike-del** - *Initial work* - [GitHub](https://github.com/dev-mike-del)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Nmap](https://nmap.org/) - This python script parses an xml file created by Nmap
