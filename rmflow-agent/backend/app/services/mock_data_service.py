from __future__ import annotations

from typing import Any

from app.data_loader import MockDataLoader, get_data_loader


class MockDataService:
    def __init__(self, loader: MockDataLoader | None = None) -> None:
        self.loader = loader or get_data_loader()

    def list_customers(self, rm_id: str | None = None) -> list[dict[str, Any]]:
        customers = self.loader.customers()
        if rm_id:
            customers = [customer for customer in customers if customer.get("rm_id") == rm_id]
        return customers

    def get_customer(self, customer_id: str) -> dict[str, Any] | None:
        return next(
            (customer for customer in self.loader.customers() if customer.get("customer_id") == customer_id),
            None,
        )

    def list_interactions(self, customer_id: str | None = None) -> list[dict[str, Any]]:
        interactions = self.loader.interactions()
        if customer_id:
            interactions = [
                interaction for interaction in interactions if interaction.get("customer_id") == customer_id
            ]
        return interactions

    def list_opportunities(self, customer_id: str | None = None) -> list[dict[str, Any]]:
        opportunities = self.loader.opportunities()
        if customer_id:
            opportunities = [
                opportunity for opportunity in opportunities if opportunity.get("customer_id") == customer_id
            ]
        return opportunities

    def list_campaigns(self, customer_id: str | None = None) -> list[dict[str, Any]]:
        campaigns = self.loader.campaigns()
        if customer_id:
            campaigns = [
                campaign
                for campaign in campaigns
                if customer_id in campaign.get("matching_customer_ids", [])
            ]
        return campaigns

    def list_products(self, product_category: str | None = None) -> list[dict[str, Any]]:
        products = self.loader.products()
        if product_category:
            products = [
                product for product in products if product.get("product_category") == product_category
            ]
        return products

    def list_templates(
        self,
        channel: str | None = None,
        product_category: str | None = None,
    ) -> list[dict[str, Any]]:
        templates: list[dict[str, Any]] = []

        for template in self.loader.email_templates():
            templates.append(
                {
                    **template,
                    "template_type": "email_template",
                    "source_id": template.get("template_id"),
                }
            )

        for script in self.loader.call_scripts():
            templates.append(
                {
                    **script,
                    "template_type": "call_script",
                    "source_id": script.get("script_id"),
                }
            )

        if channel:
            templates = [template for template in templates if template.get("channel") == channel]

        if product_category:
            templates = [
                template
                for template in templates
                if template.get("product_category") == product_category
            ]

        return templates

    def list_audit_logs(self) -> list[dict[str, Any]]:
        return []


def get_mock_data_service() -> MockDataService:
    return MockDataService()
