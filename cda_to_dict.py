from lxml import etree

def cda_to_dict(cda_file):
    """
    Convert a CDA XML file to a dictionary structure.
    
    :param cda_file: Path to the CDA XML file.
    :return: Dictionary representation of the CDA.
    """
    tree = etree.parse(cda_file)
    root = tree.getroot()

    def strip_namespace(tag):
        return tag.split('}', 1)[-1] if '}' in tag else tag

    def element_to_dict(element):
        if isinstance(element, etree._Comment):
            return None  # Skip comment nodes
        
        tag = strip_namespace(element.tag)
        data = {tag: {} if element.attrib else None}
        children = list(element)
        if children:
            dd = {}
            for dc in map(element_to_dict, children):
                if dc is not None:
                    for k, v in dc.items():
                        if k in dd:
                            if not isinstance(dd[k], list):
                                dd[k] = [dd[k]]
                            dd[k].append(v)
                        else:
                            dd[k] = v
            data[tag] = dd
        if element.attrib:
            data[tag].update((strip_namespace(k), v) for k, v in element.attrib.items())
        if element.text and element.text.strip():
            text = element.text.strip()
            if children or element.attrib:
                if text:
                    data[tag]['#text'] = text
            else:
                data[tag] = text
        return data

    cda_dict = element_to_dict(root)
    return cda_dict

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python cda_to_dict.py <cda_file>")
    else:
        cda_file = sys.argv[1]
        cda_dict = cda_to_dict(cda_file)
        print(cda_dict)