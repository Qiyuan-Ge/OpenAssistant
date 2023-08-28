from PIL import Image
import streamlit as st

st.set_page_config(page_title="Support us", page_icon="☕")

st.markdown(
    """
    ## Join the Open Assistant Heroes!
    
    Ahoy, dear user! ⚓ Thank you for embarking on this AI adventure with Open Assistant. Your support is like wind in our sails, propelling us forward on our quest for knowledge. If you're ready to become an Open Assistant Hero and help us chart new territories, here's how:

    ### **1. Unleash the Power of Stars on GitHub⭐**
    Lend us your support with the click of a star! Show your love for Open Assistant by starring our GitHub repository. It's a small action that makes a mighty impact, helping us chart a course for even greater horizons.
    
    [Star on GitHub](https://github.com/Qiyuan-Ge/OpenAssistant)
    
    ### **2. Aye, Patreon Support🏴‍☠️**
    Ye can earn a place on the Patron's deck! As a loyal patron, you'll enjoy exclusive treasures and rewards. Every piece of eight ye contribute will directly fund new features and enhancements for the ship – I mean, app.
    
    [Join on Patreon](https://www.patreon.com/OpenAssistant42)

    ### **3. WeChat Pay💰**
    Drop anchor with WeChat Pay and show yer support(有点中二，哈哈)!
    
    [查看微信支付码](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/wechat_support.png)
    
    Yarrr, with your backing, we'll keep the cannons... err, algorithms firing smoothly, raise the sails of innovation, and ensure you have a swashbucklin' good time with Open Assistant. Our hearty thanks for your generosity, and watch out for more treasures on the horizon!

    May the constellations align in your favor,  
    The Open Assistant Crew 🌠

    """
)


image = Image.open('./assets/assistant.png')
st.image(image, caption='Wish everyone can have their own AI assistant', width=256)