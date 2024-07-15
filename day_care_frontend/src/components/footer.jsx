const Footer = () => {
  return (
    <div className='bg-[#522D8C] py-10 mt-12 about'>
      <div className="max-w-6xl mx-auto w-full flex justify-end tab:justify-between items-center">
        <div className="hidden tab:flex items-center text-white text-sm text-light">
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Home</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">About Us</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Our Program</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Enrollment</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">School Calender</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Director&apos;s Corner</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Gallery</p> {"/"}
          <p className="mx-2 hover:text-[#EF8742] cursor-pointer">Contact</p>
        </div>
        <div className="flex">
          <img src="https://res.cloudinary.com/dmkjaieb2/image/upload/v1720777814/ephx5k3ygdr5r1rzxrgc.png" alt="" className='w-48 h-24'/>
        </div>
      </div>

      <div className="max-w-6xl mx-auto text-white text-sm px-3 mt-4 tab:mt-0">
        <p className="text-center tab:text-left text-lg">
        &#169; Copyright 2024 Wonderbee DayCare. 
        </p>
      </div>
    </div>
  )
}

export default Footer
