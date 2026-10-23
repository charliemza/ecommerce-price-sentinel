import json
import os
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class CompetitorQuote:
    competitor: str
    price: float

@dataclass
class ProductAudit:
    sku: str
    name: str
    target_price: float
    competitors: List[CompetitorQuote]

    @property
    def lowest_competitor(self) -> CompetitorQuote:
        return min(self.competitors, key=lambda c: c.price)

    @property
    def price_gap(self) -> float:
        return round(self.target_price - self.lowest_competitor.price, 2)

    @property
    def gap_percentage(self) -> float:
        if self.lowest_competitor.price == 0:
            return 0.0
        return round((self.price_gap / self.lowest_competitor.price) * 100, 1)

    @property
    def status(self) -> str:
        pct = self.gap_percentage
        if pct > 15.0:
            return "CRITICAL OVERPRICE"
        elif pct > 8.0:
            return "BUY BOX LOSS"
        elif pct < -5.0:
            return "COMPETITIVE ADVANTAGE"
        return "BALANCED"


def run_sample_audit():
    sample_data = [
        ProductAudit(
            sku="ON-WHEY-227",
            name="Optimum Nutrition Gold Standard Whey 2.27kg",
            target_price=89.99,
            competitors=[CompetitorQuote("Nutritienda", 79.90), CompetitorQuote("Bulevip", 81.50)]
        ),
        ProductAudit(
            sku="DYM-ISO-220",
            name="Dymatize ISO 100 Hydrolyzed 2.20kg",
            target_price=74.99,
            competitors=[CompetitorQuote("Nutritienda", 62.99), CompetitorQuote("Bulevip", 64.90)]
        ),
        ProductAudit(
            sku="AMX-CREATINA-750",
            name="Amix Creatina Monohidrato Promo 750g",
            target_price=53.90,
            competitors=[CompetitorQuote("Bulevip", 35.32), CompetitorQuote("Nutritienda", 39.95)]
        ),
        ProductAudit(
            sku="SCT-WHEY-235",
            name="Scitec 100% Whey Professional 2.35kg",
            target_price=76.49,
            competitors=[CompetitorQuote("Bulevip", 71.90), CompetitorQuote("Nutritienda", 72.50)]
        ),
        ProductAudit(
            sku="UNI-ANIMAL-44",
            name="Universal Animal Pak 44 Packs",
            target_price=54.90,
            competitors=[CompetitorQuote("Nutritienda", 51.95), CompetitorQuote("Bulevip", 52.90)]
        ),
    ]

    print("=" * 95)
    print(" E-COMMERCE PRICE SENTINEL - AUDIT DISCREPANCY MATRIX")
    print("=" * 95)
    header = "{:<16} | {:<35} | {:<9} | {:<10} | {:<12} | {}".format("SKU", "PRODUCT NAME", "MY STORE", "RIVAL BEST", "DIFF", "STATUS")
    print(header)
    print("-" * 95)

    for item in sample_data:
        best = item.lowest_competitor
        diff_str = "+{:.2f} EUR (+{:.1f}%)".format(item.price_gap, item.gap_percentage)
        row = "{:<16} | {:<35} | {:>6.2f} EUR | {:>6.2f} EUR | {:<12} | {}".format(
            item.sku, item.name[:35], item.target_price, best.price, diff_str, item.status
        )
        print(row)

    print("-" * 95)
    print("Want 24/7 continuous tracking, WhatsApp alerts & automated repricing?")
    print("Visit https://thinkconnect.com.ar/radar-precios or contact carlos@thinkconnect.com.ar")
    print("=" * 95)

if __name__ == '__main__':
    run_sample_audit()
