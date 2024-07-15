const About = () => {
  return (
    <div className="w-full grid grid-cols-1 md:grid-cols-3 gap-x-6 px-2 gap-y-4 items-center md:items-start justify-items-center justify-center">
      <div className="w-full col-span-2 rounded-md bg-white p-6">
        <h1 className="text-[#522D8C] text-xl sm:text-3xl font-extralight">
          Welcome to Wonderbee Daycare
        </h1>
        <div className="space-y-5 about text-sm sm:text-base mt-4">
          <p>
          At WonderBee Daycare, we understand the unique values and aspirations of Black African families. 
          Located in the heart of major cities across Africa, we are dedicated to providing a safe, 
          nurturing, and stimulating environment where your child can thrive. 
          Our goal is to support the development of your child’s social, emotional, physical, and cognitive skills. 
          We believe that children learn best through play and exploration, and we provide a variety of activities to encourage learning and growth.
          </p>
          <p>
          Our nurturing environment has been designed to give children the opportunity to explore, play and learn according to their individual needs. We work together with parents to provide the love and support needed for each child to reach their milestones. We are dedicated to creating and maintaining a positive learning environment for all children.
          </p>
        </div>
        <h1 className="mt-3 text-[#522D8C] text-xl sm:text-2xl">**Coming Soon - Open House and Enrollment**</h1>

        <div className="mt-5">
          <h1 className="text-xl text-[#EF8742]">Highlights / Quick Facts</h1>
          <ul className="mt-2 space-y-2">
            <li className="before:left-0 before:top-1.5 relative before:absolute before:w-2 before:h-2 before:bg-[#1BB869] about pl-4 text-sm">All-Inclusion Tuition</li>
            <li className="before:left-0 before:top-1.5 relative before:absolute before:w-2 before:h-2 before:bg-[#1BB869] about pl-4 text-sm">Safe and Secure</li>
            <li className="before:left-0 before:top-1.5 relative before:absolute before:w-2 before:h-2 before:bg-[#1BB869] about pl-4 text-sm">Development Appriopriate Curriculum</li>
            <li className="before:left-0 before:top-1.5 relative before:absolute before:w-2 before:h-2 before:bg-[#1BB869] about pl-4 text-sm">Nutritious Meals and Snacks</li>
            <li className="before:left-0 before:top-1.5 relative before:absolute before:w-2 before:h-2 before:bg-[#1BB869] about pl-4 text-sm">Qualified, Caring, ans Experienced Staff</li>
          </ul>
        </div>

        <div className="mt-4 text-sm md:text-base">
          <p className="about">
          Please sign up to receive important information about our upcoming <span className="italic font-semibold">Open House</span> using the Inquiry Form in the <a href="#" className="text-blue-400">contact us</a> section. We look forward to meeting you and your children.
          </p>
        </div>

        <div className="mt-5 px-10 py-1 bg-[#1ABE67] -ml-8 float-left bg-[url(https://purpledovespreschool.com/images/learnMorBg.jpg)] bg-right-top bg-no-repeat text-white text-sm">
          LEARN MORE ABOUT OUR PROGRAM
        </div>
      </div>
      <div className="mx-auto w-full flex items-center justify-center">
        <img src="https://purpledovespreschool.com/images/v08.png" alt="" className="!m-auto"/>
      </div>
    </div>
  )
}

export default About
