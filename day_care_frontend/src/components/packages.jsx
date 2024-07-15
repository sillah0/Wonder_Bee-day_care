const Packages = () => {
  return (
    <div className="w-full grid grid-cols-1 max-w-sm md:max-w-full mx-auto md:grid-cols-3 gap-6 mt-7 about px-2 items-start">
      <div className='flex flex-col group-colors group news relative rounded-md shadow shadow-blue-300'>
        <div className='w-full rounded relative'>
          <div className="-left-0.5 top-4 absolute w-fit text-white font-semibold text-xs bg-no-repeat bg-cover px-6 py-1 bg-[url(https://purpledovespreschool.com/images/heading3.png)] bg-[100%]">
            OUR PROGRAM
          </div>
          <img
            src={'https://purpledovespreschool.com/images/hmLstPic5.jpg'}
            className='object-cover object-center w-full h-full rounded-t-md'
          />
        </div>
        <div className='flex flex-col px-4 py-4 bg-white transition-colors duration-300 space-y-4 rounded-b-md'>
          <p className='text-base font-normal mt-3 text-[#2f2f2f]'>We invite you to learn about our preschool program</p>
          <div className="flex justify-end items-center">
            <button className="text-[.7rem] border px-3 py-1 rounded text-[#808080] bg-[#f9f9f9] hover:bg-[#d7d7d7] hover:text-black font-semibold tracking-wider">
              LEARN MORE
            </button>
          </div>
        </div>
      </div>

      <div className='flex flex-col group-colors group news relative rounded-md shadow shadow-blue-300'>
        <div className='w-full rounded relative'>
          <div className="-left-0.5 top-4 absolute w-fit text-white font-semibold text-xs bg-no-repeat bg-cover px-6 py-1 bg-[url(https://purpledovespreschool.com/images/heading2.png)] bg-[100%]">
            ABOUT US
          </div>
          <img
            src={'https://purpledovespreschool.com/images/hmLstPic4.jpg'}
            className='object-cover object-center w-full h-full rounded-t-md'
          />
        </div>
        <div className='flex flex-col px-4 py-4 bg-white transition-colors duration-300 space-y-4 rounded-b-md'>
          <p className='text-base font-normal mt-3 text-[#2f2f2f]'>Learn about our teaching and care philosophies and meet our caregivers.</p>
          <div className="flex justify-end items-center">
            <button className="text-[.7rem] border px-3 py-1 rounded text-[#808080] bg-[#f9f9f9] hover:bg-[#d7d7d7] hover:text-black font-semibold tracking-wider">
              LEARN MORE
            </button>
          </div>
        </div>
      </div>

      <div className='flex flex-col group-colors group news relative rounded-md shadow shadow-blue-300'>
        <div className='w-full rounded relative'>
          <div className="-left-0.5 top-4 absolute w-fit text-white font-semibold text-xs bg-no-repeat bg-cover px-6 py-1 bg-[url(https://purpledovespreschool.com/images/heading1.png)] bg-[100%]">
            OUR PROGRAM
          </div>
          <img
            src={'https://purpledovespreschool.com/images/hmLstPic6.jpg'}
            className='object-cover object-center w-full h-full rounded-t-md'
          />
        </div>
        <div className='flex flex-col px-4 py-4 bg-white transition-colors duration-300 space-y-4 rounded-b-md'>
          <p className='text-base font-normal mt-3 text-[#2f2f2f]'>See our tuition costs and learn how to enroll your child.</p>
          <div className="flex justify-end items-center">
            <button className="text-[.7rem] border px-3 py-1 rounded text-[#808080] bg-[#f9f9f9] hover:bg-[#d7d7d7] hover:text-black font-semibold tracking-wider">
              LEARN MORE
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Packages
