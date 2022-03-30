import warnings
import requests
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore", category=UserWarning)

class npm_analyser(object):

    def __init__(self, package_name):
        self.package_name = package_name
        if self._get_package_sanity() == False:
            raise SystemExit('NPM Package not found!')
        self.version = self._version()
        self.last_published = self._last_published()
        self.number_of_dependents = self._number_of_dependents()
        self.get_dev_dependencies = self._get_dev_dependencies()
        self.total_versions = self._total_versions()
        self.license = self._license()
        self.unpacked_size = self._unpacked_size()
        self.weekly_downloads = self._weekly_downloads()
        self.total_files = self._total_files()
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __repr__(self):
        return "%s" % (self.package_name)

    def __str__(self):
        return "%s" % (self.package_name)
    
    def _get_package_sanity(self):
        package_status = requests.get(f"https://www.npmjs.com/package/{self.package_name}")
        return True if package_status.status_code == 200 else False

    def _package_parcer(self):
        page = requests.get(f"https://www.npmjs.com/package/{self.package_name}")
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    
    def _version(self):
        soup = self._package_parcer()
        try:
            tag = soup.find_all('meta')[-1].get("content", None)
            return str(tag.split('Latest version: ')[1]).split(',')[0]
        except:
            return None
    
    def _weekly_downloads(self):
        soup = self._package_parcer()
        for sub_tag in soup.find_all('h3'):
            content = sub_tag.get_text()
            if content.endswith('Downloads'):
                return sub_tag.findNext('p').get_text() 
            
    def _license(self):
        soup = self._package_parcer()
        for sub_tag in soup.find_all('h3'):
            content = sub_tag.get_text()
            if content.startswith('License'):
                return sub_tag.findNext('p').get_text()
            
    def _unpacked_size(self):
        soup = self._package_parcer()
        for sub_tag in soup.find_all('h3'):
            content = sub_tag.get_text()
            if content.startswith('Unpacked Size'):
                return sub_tag.findNext('p').get_text()
    
    def _total_files(self):
        soup = self._package_parcer()
        for sub_tag in soup.find_all('h3'):
            content = sub_tag.get_text()
            if content.startswith('Total Files'):
                return sub_tag.findNext('p').get_text()
    
    def _last_published(self):
        soup = self._package_parcer()
        tag = soup.find_all('meta')[-1].get("content", None)
        return str(tag.split('last published: ')[1]).split('.')[0]   
    
    def _number_of_dependents(self):
        soup = self._package_parcer()
        tag = soup.find_all('meta')[-1].get("content", None)
        return str(tag.split('There are ')[1]).split(' ')[0]
    
    def _get_dev_dependencies(self):
        soup = self._package_parcer()
        try:
            return str(soup.find_all('script')[0]).split('''devDependencies":{''')[1].split('''}''')[0]
        except:
            return None
            
    def _total_versions(self):
        soup = self._package_parcer()
        return str(soup.find_all('span')).split(' Versions')[0].split('>')[-1]