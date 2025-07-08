// 📁 app/layout.tsx
import "./globals.css";
import Favicon from "@/components/Favicon";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

import { ReactNode } from "react";
import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import {
  ConnectionProvider,
  WalletProvider,
} from "@solana/wallet-adapter-react";
import { WalletModalProvider } from "@solana/wallet-adapter-react-ui";
import { getPhantomWallet, getSolflareWallet } from "@solana/wallet-adapter-wallets";

export const metadata = {
  title: "Optik Coin",
  description: "AI-powered DeFi, trading, minting & GPT-driven crypto tools",
};

const network = WalletAdapterNetwork.Mainnet;
const endpoint = "https://api.mainnet-beta.solana.com";

// add any wallets you’d like supported here
const wallets = [getPhantomWallet(), getSolflareWallet()];

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head>
        <Favicon />
      </head>
      <body className="bg-background text-foreground antialiased">
        <ConnectionProvider endpoint={endpoint}>
          <WalletProvider wallets={wallets} autoConnect>
            <WalletModalProvider>
              <Header />
                <main className="container py-8">{children}</main>
              <Footer />
            </WalletModalProvider>
          </WalletProvider>
        </ConnectionProvider>
      </body>
    </html>
  );
}
