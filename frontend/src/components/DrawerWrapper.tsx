import React from 'react'

interface DrawerWrapperProps {
  children: React.ReactNode
}

export const DrawerWrapper = (props: DrawerWrapperProps) => {
  return <>{props.children}</>
}
