// 子コンポーネントをフェードインさせるアニメーションを付与するラッパーコンポーネント
// 以下サイトを参照して作成した。
// https://zenn.dev/cureapp/articles/63c399916396b6

import React from 'react'
import { useInView } from 'react-intersection-observer'

interface FadeInBottomWrapperProps {
  children: React.ReactNode
}

export const FadeInBottomWrapper: React.FC<FadeInBottomWrapperProps> = ({ children }: FadeInBottomWrapperProps) => {
  const { ref, inView } = useInView({
    // ref要素が画面に入って100px過ぎたら発火
    rootMargin: '-100px',
    // 一度だけ発火
    triggerOnce: true,
  })

  const fadeInClassName = inView
    ? 'animate-fade-down animate-once animate-duration-1000 animate-delay-500'
    : 'opacity-0'

  const wrappedChildren = React.Children.map(children, (child) => {
    if (React.isValidElement(child)) {
      const className = [child.props.className, fadeInClassName].filter((el) => el).join(' ')

      return React.cloneElement(child as React.ReactElement, {
        ref,
        className,
      })
    } else {
      return child
    }
  })

  return <>{wrappedChildren}</>
}
