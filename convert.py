#!/usr/bin/python3

from pathlib import Path
from sys import argv
import glob
import subprocess
import xml.etree.ElementTree as ET

def extract_mediawiki(mediawiki_xml, mediawiki_dir):
    """Extract indivual mediawiki text files from a raw mediawiki XML dump."""
    print('Extracting ' + mediawiki_xml + ' into ' + mediawiki_dir + ' directory.')
    tree = ET.parse(mediawiki_xml)
    root = tree.getroot()
    ns = {'mediawiki': 'http://www.mediawiki.org/xml/export-0.3/'}
    for page in root.findall('mediawiki:page', ns):
        title = page.find('mediawiki:title', ns).text
        text = page.find('mediawiki:revision/mediawiki:text', ns).text
        output = Path(mediawiki_dir, title + '.wiki')
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text)

def convert_to_markdown(mediawiki_dir, markdown_dir):
    """Convert all the .wiki files in mediawiki_dir to .md files in markdown_dir."""
    for entry in glob.iglob(mediawiki_dir + '**/*.wiki', recursive=True):
        input = Path(entry)
        output = Path(markdown_dir, Path(entry).relative_to(mediawiki_dir)).with_suffix('.md')
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['/home/dewitt/src/pandoc-2.1.3/bin/pandoc', input, '-o', output, '--from', 'mediawiki', '--to', 'gfm'])
        
if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage convert mediawiki.xml mediawiki_dir/ markdown_dir/')
    else:
        script, mediawiki_xml, mediawiki_dir, markdown_dir = argv
        extract_mediawiki(mediawiki_xml, mediawiki_dir)
        convert_to_markdown(mediawiki_dir, markdown_dir)
