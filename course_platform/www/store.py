import frappe


def get_context(context):
	context.courses = frappe.get_all(
		"Course",
		fields=[
			"title",
			"description",
			"price",
			"route",
			"publisher.creator as publisher_creator",
			"category.title as category_title"

		],
		# filters={"is_published": True},
	)
