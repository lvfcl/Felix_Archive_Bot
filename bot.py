import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile
from config import BOT_TOKEN, GROUP_ID, IMAGE_FOLDER

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

SENT_IMAGES_FILE = "sent_images.txt"


def load_sent_images():
    if os.path.exists(SENT_IMAGES_FILE):
        with open(SENT_IMAGES_FILE, "r") as file:
            return set(line.strip() for line in file)
    return set()


def save_sent_image(image_name):
    with open(SENT_IMAGES_FILE, "a") as file:
        file.write(image_name + "\n")


async def send_images_to_group():
    sent_images = load_sent_images()

    while True:
        images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.mp4', 'jfif'))]
        
        for image_name in images:
            if image_name in sent_images:
                continue
            
            image_path = os.path.join(IMAGE_FOLDER, image_name)
            try:
                image_file = FSInputFile(image_path)
                await bot.send_photo(chat_id=GROUP_ID, photo=image_file)

                save_sent_image(image_name)
                sent_images.add(image_name)
            except Exception as e:
                print(f"Ошибка отправки {image_name}: {e}")

        await asyncio.sleep(1800)  


async def main():
    asyncio.create_task(send_images_to_group())
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

