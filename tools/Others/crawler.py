import requests  # requests是一个用于发送HTTP请求的 第三方库。
from bs4 import BeautifulSoup  # 三方库bs4中的一个类BeautifulSoup,为后续可以直接使用，不需要再通过bs4.BeautifulSoup的形式调用，让代码更简洁。
import time  # 内置库


def crawl_website(url):
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发送GET请求
        response = requests.get(url, headers=headers, timeout=10)  #get是requests里的一个顶层函数。
        # 检查请求是否成功
        response.raise_for_status()
        # 设置正确的编码
        response.encoding = response.apparent_encoding

        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 这里以提取网页标题和所有链接为例
        title = soup.title.string if soup.title else '无标题'
        print(f"网页标题: {title}")

        # 提取所有链接
        links = soup.find_all('a')
        print(f"\n发现{len(links)}个链接:")
        for i, link in enumerate(links[:10], 1):  # 只显示前10个链接
            href = link.get('href')
            text = link.get_text(strip=True)
            print(f"{i}. 文本: {text}, 链接: {href}")

        return True

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return False
    finally:
        # 延迟一段时间，避免给服务器造成过大压力
        time.sleep(2)


if __name__ == "__main__":
    # 这里替换为你要爬取的合法网页URL
    target_url = "https://example.com"  # example.com是一个用于示例的合法网站
    print(f"开始爬取 {target_url}...")
    crawl_website(target_url)
