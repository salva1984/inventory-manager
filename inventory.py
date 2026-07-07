
from __future__ import annotations

import argparse


from product import build_product, format_product
from storage import load_products, save_products
from inventory_service import (
    list_products,
    add_product,
    remove_product,
    get_total_value

)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inventory Manager")
    parser.add_argument("--storage", default="inventory.json", help="JSON storage file")

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new product")
    add_parser.add_argument("--id", required=True)
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--quantity", required=True, type=int)
    add_parser.add_argument("--price", required=True, type=float)
    add_parser.add_argument("--category", required=True)

    subparsers.add_parser("list", help="List all products")
    subparsers.add_parser("total", help="Show the total value of all products")

    update_parser = subparsers.add_parser("update", help="Update product quantity")
    update_parser.add_argument("--id", required=True)
    update_parser.add_argument("--quantity", required=True, type=int)

    remove_parser = subparsers.add_parser("remove", help="Remove a product")
    remove_parser.add_argument("--id", required=True)

    return parser

def run(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    products = load_products(args.storage)

    try:
        if args.command == "add":
            products = add_product(
                products,
                build_product(
                    args.id,
                    args.name,
                    args.description,
                    args.quantity,
                    args.price,
                    args.category,
                ),
            )
            save_products(products, args.storage)
            print(f"Added product '{args.id}'")

        elif args.command == "list":
            current_products = list_products(products)
            if not current_products:
                print("No products found")
            else:
                for product in current_products:
                    print(format_product(product))

        elif args.command == "remove":
            products = remove_product(products, args.id)
            save_products(products, args.storage)
            print(f"Removed product '{args.id}'")

        elif args.command == "total":
            print(f"Total inventory value: {get_total_value(products):.2f}")
        
    except ValueError as error:
        print(error)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(run())
