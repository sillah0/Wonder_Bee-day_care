import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, EffectFade, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/effect-fade';
import { TfiAngleLeft, TfiAngleRight } from 'react-icons/tfi';

const Carousel = () => {
  return (
    <div className='w-full h-fit xs:h-fit relative my-5'> 
      <Swiper
        autoplay={{
          delay: 5000
        }}
        spaceBetween={30}
        loop={true}
        navigation={{
          nextEl: '.custom-button-next',
          prevEl: '.custom-button-prev',
        }}
        effect={'fade'}
        pagination={{
          clickable: true,
        }}
        modules={[EffectFade, Navigation, Pagination, Autoplay]}
        className="relative h-[300px] xs:h-fit w-full"
      >
        <SwiperSlide className=''>
          <img src="https://purpledovespreschool.com/images/slider0.png" className='h-full w-full object-cover object-center'/>
        </SwiperSlide>
        <SwiperSlide className=''>
          <img src="https://purpledovespreschool.com/images/slider1.png" className='h-full w-full object-cover object-center'/>
        </SwiperSlide>
        <SwiperSlide className=''>
          <img src="https://purpledovespreschool.com/images/slider5.png" className='h-full w-full object-cover object-center'/>
        </SwiperSlide>
        <SwiperSlide className=''>
          <img src="https://purpledovespreschool.com/images/slider8.png" className='h-full w-full object-cover object-center'/>
        </SwiperSlide>
        <SwiperSlide className='relative'>
          <img src="https://purpledovespreschool.com/images/slider9.png" className='h-full w-full object-cover object-center'/>
        </SwiperSlide>
          <div className='w-full bottom-2 tab:h-80 tab:top-1/4 tab:left-20 absolute z-[100] max-w-full tab:max-w-md flex flex-col items-center justify-center space-y-2 tab:space-y-4'>
            <h1 className='text-[#FFF9BE] text-center tracking-wider [text-shadow:_0_1px_0_rgb(0_0_0_/_40%)] text-xl tab:text-4xl leading-snug'>
              High-Quality Child Care & Early Education
            </h1>  
            <p className='text-2xl tab:text-4xl font-semibold text-white tracking-wider drop-shadow-2xl [text-shadow:_0_1px_0_rgb(0_0_0_/_40%)]'>
              LEARN. PLAY. GROW.
            </p>

            <a href='' className='bg-no-repeat bg-contain bg-center bg-[url(https://purpledovespreschool.com/images/bannerBtnBg.png)] w-full h-12 lg:h-20 flex items-center justify-center text-white uppercase text-xl tab:text-3xl'>
              inquire now
            </a>
          </div>
      </Swiper>
      <div 
      className="absolute z-10 p-2 text-white transform -translate-y-1/2 bg-gray-800 bg-opacity-50 rounded-full cursor-pointer custom-button-next top-1/2 right-4 hover:bg-gray-600 group">
        <TfiAngleRight size={20} className='text-[#b1b0b0] group-hover:text-white'/>
      </div>
      <div 
      className="absolute z-10 p-2 text-white transform -translate-y-1/2 bg-gray-800 bg-opacity-50 rounded-full cursor-pointer custom-button-prev top-1/2 left-4 hover:bg-gray-600 group">
      <TfiAngleLeft size={20} className='text-[#b1b0b0] group-hover:text-white'/>
      </div>
    </div>
  )
}

export default Carousel
