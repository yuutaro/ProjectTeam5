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
        <div className="navbar bg-base-300 w-full">
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
          <div className="mx-2 flex-1 px-2">Navbar Title</div>
          <div className="hidden flex-none lg:block">
            <ul className="menu menu-horizontal">
              {/* Navbar menu content here */}
              <li>
                <a>Navbar Item 1</a>
              </li>
              <li>
                <a>Navbar Item 2</a>
              </li>
              <li>
                <ThemeSelector />
              </li>
            </ul>
          </div>
        </div>
        {/* Page content here */}
        <div className="btn btn-primary" onClick={handleToggle}></div>
        {isOpen && <p className=" text-right">true</p>}
        {props.children}
      </div>
      <div className="drawer-side">
        <label htmlFor="my-drawer-3" aria-label="close sidebar" className="drawer-overlay"></label>
        <ul className="menu bg-base-200 min-h-full w-80 p-4">
          {/* Sidebar content here */}
          <li>
            <a>Sidebar Item 1</a>
          </li>
          <li>
            <a>Sidebar Item 2</a>
          </li>
          <li>
            <ThemeSelector />
          </li>
          <li>
            <label htmlFor="my-drawer-3" className="btn btn-ghost">
              Close
            </label>
          </li>
        </ul>
      </div>
    </div>
  )
}
