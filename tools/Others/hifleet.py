import requests
from bs4 import BeautifulSoup
import time
import random


class PortRouteCrawler:
    def __init__(self):
        self.base_url = "https://www.hifleet.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
        # 控制爬取速度，避免被反爬
        self.delay_range = (1, 3)

    def get_port_page(self):
        """获取港口页面内容"""
        url = f"{self.base_url}/port/index.html"
        try:
            # 随机延迟，模拟人类浏览行为
            time.sleep(random.uniform(*self.delay_range))
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # 抛出HTTP错误状态码
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"获取港口页面失败: {e}")
            return None

    def parse_port_list(self, html_content):
        """解析港口列表"""
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        ports = []

        # 这里的选择器需要根据实际页面结构调整
        port_elements = soup.select('div.port-item')  # 假设港口项有port-item类

        for element in port_elements:
            try:
                # 提取港口名称和链接，选择器需根据实际页面调整
                name = element.select_one('h3.port-name').text.strip()
                link = element.select_one('a')['href']
                # 确保链接是完整的
                if link.startswith('/'):
                    link = f"{self.base_url}{link}"
                ports.append({
                    'name': name,
                    'url': link
                })
            except Exception as e:
                print(f"解析港口信息出错: {e}")
                continue

        return ports

    def get_route_info(self, from_port_url, to_port_url):
        """尝试获取两个港口之间的航线信息"""
        # 这里需要根据实际网站的航线查询机制调整
        # 可能是通过API接口或表单提交，需要分析网络请求
        try:
            # 随机延迟
            time.sleep(random.uniform(*self.delay_range))

            # 假设网站有航线查询API
            route_url = f"{self.base_url}/api/route"
            params = {
                'from': from_port_url.split('/')[-1],  # 提取港口ID
                'to': to_port_url.split('/')[-1],
                'type': 'sea'
            }

            response = requests.get(route_url, params=params, headers=self.headers)
            response.raise_for_status()

            # 假设返回JSON数据
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"获取航线信息失败: {e}")
            return None

    def run(self, from_port_name, to_port_name):
        """主函数：获取从出发港到目的港的航程"""
        print(f"正在查询从 {from_port_name} 到 {to_port_name} 的航程...")

        # 获取港口页面
        port_html = self.get_port_page()
        if not port_html:
            return None

        # 解析港口列表
        ports = self.parse_port_list(port_html)
        if not ports:
            print("未找到港口信息")
            return None

        # 查找出发港和目的港的URL
        from_port = next((p for p in ports if from_port_name in p['name']), None)
        to_port = next((p for p in ports if to_port_name in p['name']), None)

        if not from_port or not to_port:
            print("未找到指定的港口")
            return None

        # 获取航线信息
        route_info = self.get_route_info(from_port['url'], to_port['url'])

        if route_info:
            print(f"成功获取从 {from_port_name} 到 {to_port_name} 的航程信息:")
            return route_info
        else:
            print("无法获取航线信息")
            return None


if __name__ == "__main__":
    crawler = PortRouteCrawler()
    # 示例：查询从上海港到新加坡港的航程
    result = crawler.run("SHANGHAI[China (Republic of)]", "Singapore[Singapore]")
    if result:
        print(result)
