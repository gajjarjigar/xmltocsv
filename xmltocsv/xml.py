from lxml import etree
from pandas import DataFrame
import os


class XML:

    def __init__(self, xml_file):
        if xml_file:
            self.xml_file = os.path.realpath(xml_file)

    def convert_to_csv(self, output_dir, row_node_name):
        parser = etree.XMLParser(encoding='utf-8', strip_cdata=False)
        xml_tree = etree.parse(self.xml_file, parser=parser)
        df = DataFrame()
        row_list = xml_tree.xpath('//{}'.format(str(row_node_name).strip()))
        for row in row_list:
            row_dict = {}
            for node in row.iter():
                if len(node):
                    continue
                else:
                    row_dict[node.tag] = node.text
            if row_dict:
                df = df.append([row_dict])

        df.index = range(len(df.index))

        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            csv_file = os.path.join(output_dir, '{}.csv'.format(os.path.basename(self.xml_file)))
            df.to_csv(csv_file, sep=',', index=False)
            return csv_file

        return None
