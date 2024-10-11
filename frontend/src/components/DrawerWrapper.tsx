import Image from 'next/image'
import Link from 'next/link'
import React, { useState } from 'react'
import { ThemeSelector } from './ThemeSelector'

interface DrawerWrapperProps {
  children: React.ReactNode
}

export const DrawerWrapper = (props: DrawerWrapperProps) => {
  const [isOpen, setIsOpen] = useState(false) // ドロワーの開閉状態を管理する state

  const handleToggle = () => {
    setIsOpen(!isOpen) // ドロワーの開閉状態を切り替える
  }

  return (
    <div className="drawer">
      <input
        id="my-drawer-3"
        type="checkbox"
        className="drawer-toggle"
        checked={isOpen} // state の値を input の checked 属性に反映
        onChange={handleToggle} // input の変更イベントで state を更新
      />
      <div className="drawer-content flex flex-col">
        {/* Navbar */}
        <div className="navbar w-full bg-opacity-0 bg-base-100 fixed top-0 z-40">
          <div className="flex-none lg:hidden">
            <label htmlFor="my-drawer-3" aria-label="open sidebar" className="btn btn-square btn-ghost">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block h-6 w-6 stroke-current"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </label>
          </div>
          {/* Logo */}
          <div>
            <Link href="/">
              <Image src="/svg/Horizontal Lines Horse.svg" width={50} height={50} alt="Horizontal Lines Horse" />
            </Link>
          </div>
          <div className="mx-2 flex-1 px-2">
            <Link href="/">PacePredict</Link>
          </div>
          <div className="hidden flex-none lg:block">
            <ul className="menu menu-horizontal space-x-8">
              {/* Navbar menu content here */}
              <li>
                <Link href="#" className="btn btn-primary w-36">
                  予測開始!!
                </Link>
              </li>
              <li>
                <Link href="#" className="btn bg-base-300 w-36">
                  about
                </Link>
              </li>
              <li>
                <ThemeSelector />
              </li>
            </ul>
          </div>
        </div>
        {/* Page content here */}
        {props.children}
      </div>
      <div className="drawer-side z-50">
        <label htmlFor="my-drawer-3" aria-label="close sidebar" className="drawer-overlay"></label>
        <div className="menu bg-base-200 h-full w-80 p-4">
          {/* sidebar content here */}
          <div className="flex flex-col justify-between h-full">
            <div className="flex flex-col space-y-4">
              <button className="btn bg-base-300 w-full" onClick={handleToggle}>
                close
              </button>
              <div>
                {/* Linkをblock化すると文字の位置がバグるためdivで囲む */}
                <Link href="#" className="btn btn-primary mt-1 text-center w-full">
                  予測開始!!
                </Link>
              </div>
              <div>
                <Link href="/mypage" className="btn bg-base-300 w-full">
                  about
                </Link>
              </div>
              <ThemeSelector />
            </div>
            <button className="btn bg-base-300 w-full" onClick={handleToggle}>
              close
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
