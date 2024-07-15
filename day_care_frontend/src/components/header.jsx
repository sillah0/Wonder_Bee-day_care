const Header = () => {
  return (
    <div className='w-full flex flex-col items-center justify-between lg:flex-row space-y-4 lg:space-y-0 px-2' id="home">
      <div className='lg:block hidden'>
        <img src="https://res.cloudinary.com/dmkjaieb2/image/upload/v1720776057/y4xq47laueivlgtjdpvj.png" alt="" className='w-72 h-72'/>
      </div>
      <div className='lg:hidden'>
        <img src="https://res.cloudinary.com/dmkjaieb2/image/upload/v1720777814/ephx5k3ygdr5r1rzxrgc.png" alt="" className='w-48 h-20 md:w-72 md:h-36'/>
      </div>
      <div className='flex flex-col w-full space-y-5 max-w-3xl p-2'>
        <div className='flex items-center justify-center lg:justify-end text-xl md:text-3xl tracking-wide lg:border-b pb-6 w-full border-b-white'>
          <p className='text-[#FFFFFF] border-r border-r-white pr-4'>Login </p>
          <a href="#" className='text-[#FFE03F] pl-4'>Sign Up</a>
          <img src='https://purpledovespreschool.com/images/headerIcon7.png' alt='maps' className='ml-4 hidden xs:flex'/>
        </div>
        <div className="xs:hidden flex items-center justify-center">
          <img src='https://purpledovespreschool.com/images/headerIcon7.png' alt='maps' className='ml-4'/>
        </div>
        <div className='lg:flex items-center justify-center space-x-3 uppercase text-lg border-b pb-6 border-b-white hidden'>
          <button className='uppercase text-white bg-[#9CBF3E] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>home</button>
          <button className='uppercase text-white bg-[#F6B63A] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>about</button>
          <button className='uppercase text-white bg-[#EF8742] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>programs</button>
          <button className='uppercase text-white bg-[#E05543] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>for parents</button>
          <button className='uppercase text-white bg-[#8869CA] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>gallery</button>
          <button className='uppercase text-white bg-[#2799C9] px-4 py-2 rounded-md hover:text-black hover:bg-white transition-colors duration-300'>contact</button>
        </div>
      </div>
    </div>
  )
}

export default Header
