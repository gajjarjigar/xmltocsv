# Standard Imports
from lxml import etree
from pandas import DataFrame
import os


class XML:

    def __init__(self, xml_file):
        if xml_file:
            # XML file path
            self.xml_file = os.path.realpath(xml_file)

    def convert_to_csv(self, output_dir, row_node_name):

        # Custom Parser to avoid stripping CDATA
        parser = etree.XMLParser(encoding='utf-8', strip_cdata=False)
        # Parse XML file
        xml_tree = etree.parse(self.xml_file, parser=parser)
        # Create Empty Data Frame
        df = DataFrame()
        # Get List of XML Nodes (Rows in CSV)
        row_list = xml_tree.xpath('//{}'.format(str(row_node_name).strip()))
        for row in row_list:
            row_dict = {}
            # Iterate through each node in the row
            for node in row.iter():
                if len(node):
                    # if node has a child then skip
                    continue
                else:
                    # Node has no child hence it must be a leaf node with data
                    row_dict[node.tag] = node.text
            if row_dict:
                df = df.append([row_dict])

        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            csv_file = os.path.join(output_dir, '{}.csv'.format(os.path.basename(self.xml_file)))
            # Convert DataFrame to csv
            df.to_csv(csv_file, sep=',', index=False)
            return csv_file

        return None
