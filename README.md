# xmltocsv
XML to CSV

## Prerequisites

    pip install pandas
    pip install lxml

## Usage

    from xmltocsv.xml import XML
    
    obj = XML('path to xml')  
    obj.convert_to_csv('path to output directory', 'row node name')

## Example

    from xmltocsv.xml import XML
    
    obj = XML('D:\\Input\\test.xml')  
    obj.convert_to_csv('D:\\Output', 'employee')


## XML File:

    <?xml version="1.0" encoding="UTF-8" ?>  
	<root>  
		 <employee>  
			 <id>IN0034</id>  
			 <name>Jigar Gajjar</name>  
			 <team>Machine Learning</team>  
		 </employee>  
		 <employee>  
			 <id>IN0035</id>  
			 <name>Shinchan Nohara</name>  
			 <team>Data Warehouse</team>  
		 </employee>  
		 <employee>  
			 <id>IN0036</id>  
			 <name>Logan</name>  
			 <team>X-Men</team>  
		 </employee>  
	</root>

CSV File:

    id,name,team
    IN0034,Jigar Gajjar,Machine Learning
    IN0035,Shinchan Nohara,Data Warehouse
    IN0036,Logan,X-Men
