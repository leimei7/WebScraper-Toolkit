import asyncio
import aiohttp
import os

async def download_image(session, url, filename):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {url}. Status code: {response.status}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


async def main():
    txt_file = 'output1.txt'
    if not os.path.exists(txt_file):
        print(f"File {txt_file} not found.")
        return

    with open(txt_file, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]

    if not os.path.exists('downloaded_images3'):
        os.makedirs('downloaded_images3')

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls, start=1):
            filename = os.path.join('downloaded_images3', f'e_{i}.jpg')
            task = asyncio.create_task(download_image(session, url, filename))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
