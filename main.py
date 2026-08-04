import asyncio
from rubika_py import Rubika
from dotenv import load_dotenv
import os

# بارگذاری تنظیمات از فایل .env
load_dotenv()

async def main():
    # گرفتن سشن از فایل .env
    session_str = os.getenv("RUBIKA_SESSION")
    
    if not session_str or session_str == "اینجا_باید_سشن_یا_توکن_روبیکا_باشد":
        print("⚠️ خطا: لطفاً ابتدا سشن روبیکا را در فایل .env وارد کنید!")
        return

    print("🚀 در حال اتصال به روبیکا...")
    
    try:
        # اتصال به روبیکا با استفاده از سشن
        client = Rubika(session=session_str)
        await client.start()
        
        print("✅ اتصال برقرار شد!")
        print(f"👤 اکانت فعلی: {await client.get_me()}")
        
        # اینجا ربات فعلاً فقط کارش اینه که وصل بشه و قطع بشه
        # در مراحل بعد، دستورات اصلی رو اینجا اضافه می‌کنیم
        
        await client.stop()
        print("👋 اتصال قطع شد.")
        
    except Exception as e:
        print(f"❌ خطای غیرمنتظره: {e}")

if __name__ == "__main__":
    asyncio.run(main())
